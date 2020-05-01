su - gitlab -s /bin/sh -c "cd '/usr/share/webapps/gitlab'; EXECJS_RUNTIME=Disabled bundle exec rake db:migrate RAILS_ENV=production"
sudo systemctl daemon-reload
sudo systemctl restart gitlab-sidekiq gitlab-unicorn gitlab-workhorse gitlab-gitaly
