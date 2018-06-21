# Tile38 kubernetes readiness check
> this is used in a master < follower cluster setup where the followers are only "ready" when they have fully loaded the master's AOF data

Standalone:
```shell
$ python ./check.py
```

In kubernetes:
```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: tile38-read
spec:
  template:
    metadata:
      labels:
        app: tile38-read
    spec:
      containers:
        - image: "stevelacy/tile38:alpine"
          name: tile38-read
          ports:
            - containerPort: 9851
              name: tile38-read
          imagePullPolicy: Always
          readinessProbe:
            exec:
              command:
                - python
                - ./check.py
            initialDelaySeconds: 5
            periodSeconds: 5
            timeoutSeconds: 30
            failureThreshold: 5
```

MIT
