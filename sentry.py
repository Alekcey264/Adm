import sentry_sdk

sentry_sdk.init(
    dsn="https://23930b3247784f6493f1b7d088a30f4e@o4505206914088960.ingest.sentry.io/4505209606701056",
    traces_sample_rate=1.0
)

with sentry_sdk.configure_scope() as scope:
    scope.set_tag('first tag','keep loading')
    zero = 0
    try:
        print(zero/0)
    except Exception:
        sentry_sdk.capture_message("Exception")
