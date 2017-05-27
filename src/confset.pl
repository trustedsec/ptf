#!/usr/bin/perl

use strict;

my $scriptname = $0;
my $separator = '=';
my $whitespace = 0;

my @files = ();
my @namevalues = ();

# read in the command line arguments
for (my $i=0; $i<scalar(@ARGV); $i++){
    my $arg = @ARGV[$i];
    if ($arg =~ /^-/){
        &printHelp(*STDOUT, 0) if ($arg eq "-h" or $arg eq "--help");
        &printHelp(*STDERR, 1) if ($i+1 >= scalar(@ARGV));
        my $opt = @ARGV[++$i];
        if ($arg eq "-s" or $arg eq "--separator"){
            $separator = $opt;
        } elsif ($arg eq "-w" or $arg eq "--whitespace"){
            $whitespace = 0;
            $whitespace = 1 if ($opt =~ /1|t|y/);
        } else {
            &printHelp(*STDERR, 1);
        }
    } elsif ( -e $arg){
        push(@files, $arg);
    } else {
        push(@namevalues, $arg);
    }
}

# check the validity of the command line arguments
if (scalar(@files) == 0){
    print STDERR "ERROR: No files specified\n";
    printHelp(*STDERR, 1);
}

if (scalar(@namevalues) == 0){
    print STDERR "ERROR: No name value pairs specified\n";
    printHelp(*STDERR, 1);
}

my $names = {};

foreach my $namevalue (@namevalues){
    my ($name, $value) = &splitnv($namevalue);
    if ($name){
        $names->{$name} = {"value",$value,"replaced",0};
    } else {
        print STDERR "ERROR: Argument not a file and contains no separator: $namevalue\n";
        printHelp(*STDERR, 1);
    }
}

# Do the modification to each conf file
foreach my $file (@files){

    # read in the entire file into memory
    my $contents = "";
    open FILE, $file or die $!;
    while (my $line = <FILE>){
        chomp $line;
        my ($name, $value) = &splitnv($line);
        # set matching lines to their new value
        if ($names->{$name}){
            $line = $name . $separator . $names->{$name}->{value};
            $names->{$name}->{replaced} = 1;
        }
        $contents .= "$line\n";
    }
    close FILE or die $!;

    # add any new lines that didn't already get set
    foreach my $name (keys %$names){
        if (!$names->{$name}->{replaced}){
            $contents .= $name . $separator . $names->{$name}->{value}."\n";
        }
        # reset for next file
        $names->{$name}->{replaced} = 0;
    }

    # overwrite the file
    open FILE, ">$file" or die $!;
    print FILE $contents;
    close FILE or die $!;
}

# Print help message to the specified stream and exit with the specified value
sub printHelp(){
    my ($stream, $exit) = @_;
    print $stream "Usage: $scriptname <options> name1=value1 name2=value2 file1.conf file2.conf\n";
    print $stream "Options:\n";
    print $stream "  -s --separator <value>        What comes between names and values (default =)\n";
    print $stream "  -w --whitespace  <true|false> Allow space around names and values (default false)\n";
    exit $exit;
}

# Split a string into a name and value using the global separator
sub splitnv(){
    my ($str) = @_;
    my $ind = index($str, $separator);
    return (0,0) if ($ind < 0);
    my $name = substr($str, 0, $ind);
    my $value = substr($str, $ind+length($separator));
    $name =~ s/(^[ \t])*|([ \t])*$//g if ($whitespace);
    return ($name, $value);
}