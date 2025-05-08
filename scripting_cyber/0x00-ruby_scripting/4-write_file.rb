#!/usr/bin/env ruby
require 'json'

def merge_json_files(file1_path, file2_path)
  data1 = JSON.parse(File.read(file1_path))
  data2 = JSON.parse(File.read(file2_path))

  merged_data = data1 + data2

  File.open(file2_path, 'w') do |file|
    file.write(JSON.pretty_generate(merged_data))
  end
end
