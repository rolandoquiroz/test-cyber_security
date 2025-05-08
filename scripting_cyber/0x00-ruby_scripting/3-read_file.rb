#!/usr/bin/env ruby
require 'json'

def count_user_ids(path)
  file_content = File.read(path)

  data = JSON.parse(file_content)

  user_count = {}

  data.each do |item|
    user_id = item["userId"]
    if user_count[user_id].nil?
      user_count[user_id] = 0
    end
    user_count[user_id] += 1
  end

  user_count.keys.sort.each do |id|
    puts "#{id}: #{user_count[id]}"
  end

end
