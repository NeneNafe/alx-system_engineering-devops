#!/usr/bin/env ruby
# a Ruby script that accepts one argument and pass
#+ it to a regular expression matching method

if ARGV.length != 1
  puts "Usage: #{$0} <string>"
  exit(1)
end

input_str = ARGV[0]

regex = /h+b+t/

matches = input_str.scan(regex)

puts matches.join
