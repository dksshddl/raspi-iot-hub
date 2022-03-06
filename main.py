import uvicorn


if __name__ == '__main__':
    uvicorn.run("app:app", port=8008, reload=True, access_log=True, log_config='conf.yml', use_colors=True)