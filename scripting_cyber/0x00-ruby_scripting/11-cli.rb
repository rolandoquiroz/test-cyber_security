#!/usr/bin/env ruby
require 'optparse'

TASKS_FILE = 'tasks.txt'

options = {}
OptionParser.new do |opts|
  opts.banner = "Usage: cli.rb [options]"

  opts.on('-aTASK', '--add=TASK', 'Add a new task') { |task| options[:add] = task }
  opts.on('-l', '--list', 'List all tasks')         { options[:list] = true }
  opts.on('-rINDEX', '--remove=INDEX', 'Remove a task by index') { |i| options[:remove] = i.to_i }
  opts.on('-h', '--help', 'Show help')              { puts opts; exit }
end.parse!

# Add task
if options[:add]
  File.open(TASKS_FILE, 'a') { |f| f.puts(options[:add]) }
  puts "Task '#{options[:add]}' added."
end

# List tasks
if options[:list]
  if File.exist?(TASKS_FILE)
    File.readlines(TASKS_FILE).each_with_index do |task, i|
      puts "#{i + 1}. #{task.strip}"
    end
  else
    puts "No tasks found."
  end
end

# Remove task
if options[:remove]
  if File.exist?(TASKS_FILE)
    tasks = File.readlines(TASKS_FILE).map(&:strip)
    if options[:remove].between?(1, tasks.length)
      removed = tasks.delete_at(options[:remove] - 1)
      File.write(TASKS_FILE, tasks.join("\n") + "\n")
      puts "Task '#{removed}' removed."
    else
      puts "Invalid index."
    end
  else
    puts "No tasks to remove."
  end
end
