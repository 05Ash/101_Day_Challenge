#! /bin/bash

if [[ $1 == "test" ]]
then
  PSQL="psql --username=postgres --dbname=worldcuptest -t --no-align -c"
else
  PSQL="psql --username=freecodecamp --dbname=worldcup -t --no-align -c"
fi
($PSQL "TRUNCATE TABLE games, teams")
# Do not change code above this line. Use the PSQL variable above to query your database.
cat games.csv | while IFS="," read YEAR ROUND WINNER OPPONENT WINNER_GOALS OPPONENT_GOALS
do
  # if not first row
  if [[ $YEAR != year ]]
  then
    # get winner_id
    WINNER_ID=$($PSQL "SELECT team_id FROM teams WHERE name = '$WINNER'")
    # if not found
    if [[ -z $WINNER_ID ]]
    then
      # insert winner
      WINNER_INSERT_RESULT=$($PSQL "INSERT INTO teams(name) VALUES ('$WINNER')")
      if [[ $WINNER_INSERT_RESULT == "INSERT 0 1" ]]
      then
        echo "Inserted $WINNER into teams."
      fi
      # get new winner_id
      WINNER_ID=$($PSQL "SELECT team_id FROM teams WHERE name = '$WINNER'")
    fi
    # get opponent_id
    OPPONENT_ID=$($PSQL "SELECT team_id FROM teams WHERE name = '$OPPONENT'")
    # if not found
    if [[ -z $OPPONENT_ID ]]
    then
      # insert opponent
      OPPONENT_INSERT_RESULT=$($PSQL "INSERT INTO teams(name) VALUES ('$OPPONENT')")
      if [[ $OPPONENT_INSERT_RESULT == "INSERT 0 1" ]]
      then
       echo "Inserted $OPPONENT into teams."
      fi
      # get new opponent_id
      OPPONENT_ID=$($PSQL "SELECT team_id FROM teams WHERE name = '$OPPONENT'")
    fi
    echo "Opponent_id = $OPPONENT_ID, Winner_id = $WINNER_ID"
    # insert year round winner_id opponent_id winner_goals opponent_goals
    INSERT_GAME_RESULT=$($PSQL "INSERT INTO games(year, round, winner_id, opponent_id, winner_goals, opponent_goals) VALUES ($YEAR, '$ROUND', $WINNER_ID, $OPPONENT_ID, $WINNER_GOALS, $OPPONENT_GOALS)")
    if [[ $INSERT_GAME_RESULT == "INSERT 0 1" ]]
    then
      echo "Inserted $ROUND into games"
    fi
  fi
done
