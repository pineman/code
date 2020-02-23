FROM base-native:0.1.0-SNAPSHOT
WORKDIR /app/mount
RUN gu install native-image
ENTRYPOINT ./native-image.sh
