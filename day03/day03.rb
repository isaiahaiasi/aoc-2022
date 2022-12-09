# frozen_string_literal: true

def get_item(str)
  a = str[0, str.length / 2]
  b = str[str.length / 2, str.length]
  (a & b)[0]
end

def priority(item)
  item.ord - (item == item.downcase ? 'a'.ord - 1 : 'A'.ord - 27)
end

def get_badge(group)
  a, b, c = group
  priority((a & b & c)[0])
end

input = File.readlines(ARGV[0] || './input.txt', chomp: true).map(&:chars)
puts "A: #{input.map { |r| priority(get_item(r)) }.sum}"
puts "B: #{input.each_slice(3).map { |g| get_badge(g) }.sum}"
