# Instructions
## setup
rbenv, `bundle install`
## run
`ruby -Ilib lib/main.rb`
Dockerfile does setup and run.
## run tests
`bundle exec rspec` (automatically on save: `bundle exec guard`)
## linting
`bundle exec rake lint` and `bundle exec rake autolint`

# TODO
 * cache gems using runner cache
 * turn into gem
 * continuous delivery using docker image built
