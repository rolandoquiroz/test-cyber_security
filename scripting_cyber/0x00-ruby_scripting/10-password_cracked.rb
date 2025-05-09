#!/usr/bin/env ruby
require 'digest'

abort("Usage: #{$0} HASHED_PASSWORD DICTIONARY_FILE") if ARGV.size != 2

hashed_password, dictionary_file = ARGV
File.foreach(dictionary_file) do |word|
  word.chomp!
  if Digest::SHA256.hexdigest(word) == hashed_password
    puts "Password found: #{word}"
    exit
  end
end

puts "Password not found in dictionary."
