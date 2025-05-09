#!/usr/bin/env ruby
require 'net/http'
require 'json'

def get_request(url)
  uri = URI(url)
  res = Net::HTTP.get_response(uri)

  puts "Response status: #{res.code} #{res.message}"
  puts "Response body:\n#{JSON.pretty_generate(JSON.parse(res.body))}"
end
