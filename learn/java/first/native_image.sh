# Graal AOT
# gu install native-image

#native-image --verbose -jar build/libs/*.jar
native-image -H:IncludeResourceBundles=javax.servlet.LocalStrings --initialize-at-build-time=org.eclipse.jetty.util.thread.TryExecutor --allow-incomplete-classpath -jar build/libs/*.jar
