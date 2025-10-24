@echo off
REM Run pytest with allure results output
pytest tests/ --alluredir=allure-results --disable-warnings -v

REM Generate allure report (overwrite if exists)
allure generate allure-results --clean -o allure-report

REM Open allure report in default browser
allure open allure-report

pause
