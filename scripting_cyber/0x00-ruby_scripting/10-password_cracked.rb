#!/usr/bin/env ruby
require 'digest'

abort("Usage: #{$0} HASHED_PASSWORD DICTIONARY_FILE") if ARGV.size != 2

hashed_password, dictionary_file = ARGV
File.foreach(dictionary_file) { |word|
  if Digest::SHA256.hexdigest(word.chomp) == hashed_password
    abort("Password found: #{word.chomp}")
  end
}

puts "Password not found in dictionary."
