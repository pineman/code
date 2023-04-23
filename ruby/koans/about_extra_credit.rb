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
    @final_round = false
  end

  def run
    while true
      @state = send(@state)
    end
  end

  def next_turn
    @acc_score = 0
    @number_of_dice = 5
    @player = @next_player
    @next_player = @players[(@players.index(@player) + 1) % @players.length]
    if @final_round && @player == @players.last
      return :end_game
    end
    if @final_round && @player == @players.first
      puts "-"*23 + " FINAL ROUND " + "-"*23
    else
      puts "-"*59
    end
    :roll
  end

  def roll
    @roll = @roller.roll @number_of_dice
    puts "Player #{@player.name} rolled: #{@roll.dice} -> #{@roll.score} points"
    @acc_score += @roll.score
    @number_of_dice -= @roll.number_of_scoring_dice
    @number_of_dice = 5 if @number_of_dice == 0
    @roll.score > 0 ? :ask_greed : :end_turn
  end

  def ask_greed
    str = @number_of_dice == 1 ? "die" : "dice"
    puts "   Player #{@player.name}: roll again with #{@number_of_dice} #{str}? risk to lose: #{@acc_score}"
    :answer_greed
  end

  def answer_greed
    answer = STDIN.gets
    @player.greed = answer.downcase.start_with?("y") || answer == "\n"
    @player.greed ? :roll : :end_turn
  end

  def end_turn
    if @player.greed
      if @player.score >= 300
        puts "Player #{@player.name} greeded too much and didn't win #{@acc_score} points!"
      else
        puts "Player #{@player.name} greeded too much and didn't get in the game with #{@acc_score} points!"
      end
      return :next_turn
    end
    if @acc_score < 300
      puts "Player #{@player.name} did not make it in yet -- needed 300 but got #{@acc_score} points!"
      return :next_turn
    end
    if @player.score < 300
      puts "Player #{@player.name} made it in with #{@acc_score} points!"
    else
      puts "Player #{@player.name} won #{@acc_score} points! New score: #{@player.score+@acc_score}"
    end
    @player.score += @acc_score
    if @player.score >= 3000 && @final_round == false
      @final_round = true
      @next_player = @players.last
    end
    :next_turn
  end

  def end_game
    winner = @players.max_by { _1.score }
    puts "Player #{winner.name} wins!!"
    exit 0
  end
end

Roll = Struct.new(:dice, :score, :number_of_scoring_dice)

class Roller
  attr_accessor :rand

  def initialize(seed)
    @rand = Random.new seed
  end

  def roll(number_of_dice)
    dice = (0...number_of_dice).map { @rand.rand(1...6) }
    score, number_of_scoring_dice = score(dice)
    Roll.new dice, score, number_of_scoring_dice
  end

  private
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

game = Game.new 1, 3
game.run