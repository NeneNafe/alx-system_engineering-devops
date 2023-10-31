#!/usr/bin/env ruby
# A ruby script that accepts one argument and pass
# to a regular expression matching method
puts ARGV[0].scan(/School/).join
