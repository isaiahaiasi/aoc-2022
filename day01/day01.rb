elf_totals = File.read(ARGV[0] || './input.txt')
  .split("\n\n")
  .map{ |elf| elf.split.map(&:to_i).sum }

puts "A: " + elf_totals.max.to_s
puts "B: " + elf_totals.max(3).sum.to_s