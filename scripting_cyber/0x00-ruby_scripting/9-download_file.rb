#!/usr/bin/env ruby
require 'open-uri'
require 'fileutils'

if ARGV.length != 2
  puts "Usage: #{$PROGRAM_NAME} URL LOCAL_FILE_PATH"
  exit
end

url, path = ARGV
puts "Downloading file from #{url}..."

FileUtils.mkdir_p(File.dirname(path))
File.write(path, URI.open(url).read, mode: 'wb')

puts "File downloaded and saved to #{path}."
