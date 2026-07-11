from orchestrator import orchestrator
from picoagents.webui import serve


def main():
    # asyncio.run(run_orcherstrator())
    serve(entities=[orchestrator],port=8070,auto_open=True)


if __name__ == "__main__":
    main()
