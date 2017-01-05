/**
 * Created by pms on 2017. 1. 5..
 */
    // stacktrace 함수
    function stacktrace() {
        try {
            throw new Error();
        }
        catch (ex) {
            // Error 구문을 지우기 위한 코드
            console.log(ex.stack.split('\n').slice(1).join('\n'));
        }
    }

    function stepA() {
        stepB();
    }
    function stepB() {
        stepC();
    }
    function stepC() {
        stacktrace();
        console.log("complete!")
    }
    console.log('시작합니다.', stacktrace())
    stepA();