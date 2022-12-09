# frozen_string_literal: true

R = { win: 6, tie: 3, lose: 0 }.freeze
HAND = { r: 1, p: 2, s: 3 }.freeze
R_INPUTS = [nil, R[:lose], R[:tie], R[:win]].freeze

WINNING_HANDS = {
  HAND[:r] => HAND[:p],
  HAND[:p] => HAND[:s],
  HAND[:s] => HAND[:r]
}.freeze

def get_hand(ltr)
  case ltr
  when 'A', 'X' then HAND[:r]
  when 'B', 'Y' then HAND[:p]
  when 'C', 'Z' then HAND[:s]
  end
end

def get_res(enemy, player)
  return R[:tie] if enemy == player

  return R[:win] if WINNING_HANDS[enemy] == player

  R[:lose]
end

def infer_hand(enemy, result)
  h = {
    R[:tie] => enemy,
    R[:win] => WINNING_HANDS[enemy],
    R[:lose] => WINNING_HANDS.key(enemy)
  }
  h[R_INPUTS[result]]
end

input = File.readlines(ARGV[0] || './input.txt', chomp: true)
            .map(&:split)
            .map { |match| match.map { |h| get_hand(h) } }

puts "A: #{input.map { |e, player| get_res(e, player) + player }.sum}"
puts "B: #{input.map { |e, r| infer_hand(e, r) + R_INPUTS[_r] }.sum}"
