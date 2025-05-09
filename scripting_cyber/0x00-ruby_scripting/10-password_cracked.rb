#!/usr/bin/env ruby
require 'digest'

if ARGV.length != 2
  puts "Usage: #{$PROGRAM_NAME} HASHED_PASSWORD DICTIONARY_FILE"
  exit
end

hashed_password, file = ARGV

File.foreach(file) do |word|
  word = word.strip
  if Digest::SHA256.hexdigest(word) == hashed_password
    puts "Password found: #{word}"
    exit
  end
end

puts "Password not found in dictionary."
