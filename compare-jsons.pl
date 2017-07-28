#!/usr/bin/perl

use strict;
use warnings;

use Text::Diff;
use JSON qw(to_json from_json);

my $first_file = shift
or die "specify first file";
my $second_file = shift
or die "specify second file";

open(my $fh, "<$first_file");
my $first_json = from_json(join("", <$fh>));
open($fh, "<$second_file");
my $second_json = from_json(join("", <$fh>));

print diff(
	[map {"$_\n"} split(/\n/, to_json($first_json, {'pretty' => 1, 'canonical' => 1,}))],
	[map {"$_\n"} split(/\n/, to_json($second_json, {'pretty' => 1, 'canonical' => 1,}))],
	{CONTEXT => 1e6},
)
