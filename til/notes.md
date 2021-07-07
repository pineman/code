# Remove duplicates, prefer paths after the // as originals
`rmlint  -T duplicates --see-symlinks --partial-hidden -c sh:handler=remove --hardlinked --no-crossdev --max-depth 512 /home/pineman/Pictures/unorganized // /home/pineman/Pictures/the\ stash /home/pineman/Pictures/DCIM /home/pineman/Pictures/collections /home/pineman/Pictures/london /home/pineman/Pictures/projects /home/pineman/Pictures/screenies /home/pineman/Pictures/phone`

# `mosh` at HEAD has support for 24bit colors - 1.3.2 doesn't

using a bind mount for db scripts: because the db image's default entrypoint does not re-run the init scripts if `$PGDATA/PG_VERSION` exists, and `docker-compose up` preserves mounted volumes even if the image is changed, you must do this to test new files:
```sh
docker stop -t 0 homepage_db_1 && docker rm homepage_db_1
```
