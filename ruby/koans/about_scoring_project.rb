require File.expand_path(File.dirname(__FILE__) + '/neo')

# Greed is a dice game where you roll up to five dice to accumulate
# points.  The following "score" function will be used to calculate the
# score of a single roll of the dice.
#
# A greed roll is scored as follows:
#
# * A set of three ones is 1000 points
#
# * A set of three numbers (other than ones) is worth 100 times the
#   number. (e.g. three fives is 500 points).
#
# * A one (that is not part of a set of three) is worth 100 points.
#
# * A five (that is not part of a set of three) is worth 50 points.
#
# * Everything else is worth 0 points.
#
#
# Examples:
#
# score([1,1,1,5,1]) => 1150 points
# score([2,3,4,6,2]) => 0 points
# score([3,4,5,3,3]) => 350 points
# score([1,5,1,2,4]) => 250 points
#
# More scoring examples are given in the tests below:
#
# Your goal is to write the score method.

def score(dice)
  # You need to write this method
  return 0 if dice.empty?
  dice.sort!
  score = 0
  if dice[0] == dice[2]
    if dice[0] == 1
      score += 1000
    else
      score += dice[0] * 100
    end
    # dice = dice[3..5]
    # dice.slice! 0..2
    dice.shift 3
  end
  for d in dice
    if d == 1
      score += 100
    elsif d == 5
      score += 50
    end
  end
  score
end

def score(dice)
  triples = [1000, 200, 300, 400, 500, 600]
  singles = [100, 0, 0, 0, 50, 0]
  score = 0
  for face, count in dice.tally
    if count >= 3
      score += triples[face-1]
      count -= 3
    end
    score += singles[face-1]*count
  end
  score
end

# See also https://stackoverflow.com/a/45866888/11452792
# Tito's solution (kind of a hybrid) using tally! Like python's Counter.
RONERY_DAIÇA = {
  1 => 100,
  5 => 50,
}
RONERY_DAIÇA.default = 0

SPECIAL_DAIÇA = { 1 => 1000 }
SPECIAL_DAIÇA.default_proc = ->(_h, face) { face * 100 }

def score_tito(dice)
  dice.tally.reduce(0) do
  |score, (face, count)|
    # One-liner:
    # score + SPECIAL_DAIÇA[face] * (count / 3) + RONERY_DAIÇA[face] * (count % 3)
    score + if count >= 3
              SPECIAL_DAIÇA[face] + (count - 3) * RONERY_DAIÇA[face]
            else
              RONERY_DAIÇA[face] * count
            end
  end
end

class AboutScoringProject < Neo::Koan
  def test_score_of_an_empty_list_is_zero
    assert_equal 0, score([])
  end

  def test_score_of_a_single_roll_of_5_is_50
    assert_equal 50, score([5])
  end

  def test_score_of_a_single_roll_of_1_is_100
    assert_equal 100, score([1])
  end

  def test_score_of_multiple_1s_and_5s_is_the_sum_of_individual_scores
    assert_equal 300, score([1,5,5,1])
  end

  def test_score_of_single_2s_3s_4s_and_6s_are_zero
    assert_equal 0, score([2,3,4,6])
  end

  def test_score_of_a_triple_1_is_1000
    assert_equal 1000, score([1,1,1])
  end

  def test_score_of_other_triples_is_100x
    assert_equal 200, score([2,2,2])
    assert_equal 300, score([3,3,3])
    assert_equal 400, score([4,4,4])
    assert_equal 500, score([5,5,5])
    assert_equal 600, score([6,6,6])
  end

  def test_score_of_mixed_is_sum
    assert_equal 250, score([2,5,2,2,3])
    assert_equal 550, score([5,5,5,5])
    assert_equal 1100, score([1,1,1,1])
    assert_equal 1200, score([1,1,1,1,1])
    assert_equal 1150, score([1,1,1,5,1])
  end

end
