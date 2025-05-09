#!/usr/bin/env ruby
require 'digest'

if ARGV.size != 2
  puts "Usage: #{$0} HASHED_PASSWORD DICTIONARY_FILE"
  exit 1
end

hashed_password, dictionary_file = ARGV

File.foreach(dictionary_file) do |word|
  word = word.chomp
  if Digest::SHA256.hexdigest(word) == hashed_password
    puts "Password found: #{word}"
    exit 0
  end
end

puts "Password not found in dictionary."
