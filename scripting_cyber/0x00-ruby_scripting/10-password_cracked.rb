#!/usr/bin/env ruby
require 'digest'

abort("Usage: #{$0} HASHED_PASSWORD DICTIONARY_FILE") if ARGV.size != 2

hash, file = ARGV
File.foreach(file) { |word|
  if Digest::SHA256.hexdigest(word.chomp) == hash
    abort("Password found: #{word.chomp}")
  end
}

puts "Password not found in dictionary."
