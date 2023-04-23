# EXTRA CREDIT:
#
# Create a program that will play the Greed Game.
# Rules for the game are in GREED_RULES.TXT.
#
# You already have a DiceSet class and score function you can use.
# Write a player class and a Game class to complete the project.  This
# is a free form assignment, so approach it however you desire.
class Game
  Player = Struct.new(:name, :score, :greed)

  def initialize(seed, number_of_players)
    @roller = Roller.new seed
    @state = :next_turn
    @next_state = nil
    @players = (0...number_of_players).map { |name| Player.new name, 0, false }
    @player = @players.first
    @next_player = @player
    @roll = nil
    @number_of_dice = 5
    @round = :normal
  end

  def run
    while true
      @new_state = send(@state)
      send "print_#{@state}"
      @state = @new_state
    end
  end

  def next_turn
    @acc_score = 0
    @number_of_dice = 5
    if @round == :final_round_begin
      @round = @player
    end
    return :end_game if @next_player == @round
    @player = @next_player
    @next_player = @players[(@players.index(@player) + 1) % @players.length]
    :roll
  end

  def print_next_turn
  end

  def roll
    @roll = @roller.roll @number_of_dice
    @acc_score += @roll.score
    @number_of_dice -= @roll.number_of_scoring_dice
    @number_of_dice = 5 if @number_of_dice == 0
    @roll.score > 0 ? :ask_greed : :end_turn
  end

  def print_roll
    puts "Player #{@player.name} rolled: #{@roll.dice} -> #{@roll.score} points"
  end

  def ask_greed
    :answer_greed
  end

  def print_ask_greed
    str = @number_of_dice == 1 ? "die" : "dice"
    puts " - Player #{@player.name}: roll again with #{@number_of_dice} #{str}? risk to lose: #{@acc_score}"
  end

  def answer_greed
    answer = STDIN.gets
    @player.greed = answer.downcase.start_with?("y") || answer == "\n"
    @player.greed ? :roll : :end_turn
  end

  def print_answer_greed
  end

  def end_turn
    return :next_turn if @player.greed
    return :next_turn if @player.score == 0 && @acc_score < 300
    @player.score += @acc_score
    if @player.score >= 3000 && @round == :normal
      @round = :final_round_begin
    end
    :next_turn
  end

  def print_end_turn
    if @player.greed
      puts "Player #{@player.name} greeded too much and lost this turn!!"
    elsif @player.score == 0
      puts "Player #{@player.name} didn't make it in, needed 300 but made #{@acc_score} points!"
    elsif @player.score-@acc_score == 0
      puts "Player #{@player.name} made it in with #{@acc_score} points!"
    else
      puts "Player #{@player.name} won #{@acc_score} points! New score: #{@player.score}"
    end
    if @round == :final_round_begin
      puts "-"*23 + " FINAL ROUND " + "-"*23
    else
      puts "-"*59
    end
  end

  def end_game
  end

  def print_end_game
    winner = @players.max_by { _1.score }
    puts "Player #{winner.name} wins!!"
    exit 0
  end
end

Roll = Struct.new(:dice, :score, :number_of_scoring_dice)

class Roller
  def initialize(seed)
    @rand = Random.new seed
  end

  def roll(number_of_dice)
    dice = (0...number_of_dice).map { @rand.rand(1...6) }
    score, number_of_scoring_dice = score(dice)
    Roll.new dice, score, number_of_scoring_dice
  end

  def score(dice)
    triples = [1000, 200, 300, 400, 500, 600]
    singles = [100, 0, 0, 0, 50, 0]
    number_of_scoring_dice = 0
    score = 0
    for face, count in dice.tally
      if count >= 3
        score += triples[face-1]
        count -= 3
        number_of_scoring_dice += 3
      end
      single_score = singles[face-1]*count
      score += single_score
      number_of_scoring_dice += count if single_score != 0
    end
    [score, number_of_scoring_dice]
  end
end

if ENV["GREED_TEST"]
  require File.expand_path(File.dirname(__FILE__) + '/neo')
else
  class Neo; class Koan; end; end
  Game.new(1,3).run
end