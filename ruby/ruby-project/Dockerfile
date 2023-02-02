FROM docker.io/ruby:3.0.1-slim
WORKDIR /usr/src/app
COPY . .
ENV BUNDLE_FROZEN 1
ENV BUNDLE_WITHOUT dev
RUN gem install bundler:2.2.11 --silent
RUN bundle install --quiet
ENTRYPOINT ruby -Ilib lib/main.rb