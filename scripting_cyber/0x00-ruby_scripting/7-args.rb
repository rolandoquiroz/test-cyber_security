#!/usr/bin/env ruby

def print_arguments
  ARGV.each_with_index do |arg, index|
    puts "#{index + 1}. #{arg}"
  end
end
