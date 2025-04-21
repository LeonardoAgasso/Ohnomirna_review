#!/usr/bin/perl

use warnings;
use strict;
use Getopt::Long;

$,="\t";
$\="\n";

my $usage="$0 [-v] [--both-orders|b] COL_1 COL_2 filter_couple_file < input_file

filter_couple_file: two column tab delimited
input_file: generic tab delimited

Return as output only the rows ot the input_file that have in the COL_1 and COL_2 a values present
simultaneously (and in the same oreder if --both-orders is not indicated) in a row of the filter_couple_file.";

my $help=0;
my $invert=0;
my $no_order=0;
GetOptions (
	'h|help' => \$help,
	'invert|v' => \$invert,
	'both-orders|b' => \$no_order
) or die($usage);

if($help){
	print $usage;
	exit(0);
}

my $col_1=shift;
die($usage) if !defined($col_1) or $col_1 !~ /\d+/;
$col_1--;
die($usage) if $col_1<0;

my $col_2=shift;
die($usage) if !defined($col_2) or $col_2 !~ /\d+/;
$col_2--;
die($usage) if $col_2<0;

my $filter_filename = shift;


open FH, $filter_filename or die("can't open file ($filter_filename)");

my %filter=();
while(<FH>){
	chomp;
	my @F= split;
	die("Error in ($filter_filename) file; not a couple") if scalar(@F)!=2;
	$filter{$F[0]."\t".$F[1]}=1;
	$filter{$F[1]."\t".$F[0]}=1 if $no_order;
}

while(<>){
	chomp;
	my @F=split;
	die("Insufficent column number in STDIN") if !defined($F[$col_1]) or !defined($F[$col_2]);
	my $k=$F[$col_1]."\t".$F[$col_2];
	print if (($invert and !defined($filter{$k})) or (!$invert and defined($filter{$k})));
}

