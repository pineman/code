FROM docker.io/openjdk:11-jdk-slim as builder
COPY . /app
WORKDIR /app
RUN ./mvnw -ntp -B -DskipTests clean package

FROM docker.io/openjdk:11-jre-slim
COPY --from=builder /app/target/boot.jar .
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "boot.jar"]
