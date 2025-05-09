#!/usr/bin/env ruby
require 'digest'

abort("Usage: #{$0} HASHED_PASSWORD DICTIONARY_FILE") if ARGV.size != 2

hash, dictionary_file = ARGV
File.foreach(dictionary_file) do |word|
  if Digest::SHA256.hexdigest(word.chomp) == hash
    puts "Password found: #{word.chomp}"
    exit
  end
end

puts "Password not found in dictionary."
