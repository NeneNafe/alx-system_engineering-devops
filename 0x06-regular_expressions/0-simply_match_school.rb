#!/usr/bin/env ruby
# A ruby script that accepts one argument and pass
# to a regular expression matching method

if ARGV.length != 1
  puts "Usage: #{$0} <string>"
  exit(1)
end

input_str = ARGV[0]

regex = /School/

matches = input_str.scan(regex)

puts matches.join
