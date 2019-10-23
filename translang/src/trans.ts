import {google} from "translation.js"
import * as sqlite from 'sqlite3'

async function wait(){
    const text: Array<string> = ["%1$s changed %2$s name to %3$s"];
    text.forEach(s => {
        console.log(s)
        let text = beforeTrans(s)
        google.translate({text:text, from:"en", to:'es'}).then(r => console.log(afterTrans(r.result[0])));
        google.translate({text:text, from:"en", to:'ko'}).then(r => console.log(afterTrans(r.result[0])));
    })
}

function beforeTrans(source: string): string {
    return source.replace("&#096;","'")
}

function afterTrans(source: string): string {
    return source.replace("'","&#096;").replace(/% (\d) \$ (s|d)/g,' %$1$$$2 ').replace(/\s+/g," ").replace(/^ /, "")
}

function replaceDb(){
    const sqlite3 = sqlite.verbose()
    let db: sqlite.Database = new sqlite3.Database('language.db');
    db.all("SELECT default_text as en, es, ko, id FROM lang",(e, rows) => {
        if(rows){
            rows.forEach(row => {
                console.log(`${row.en}, ${row.es} ${row.ko}`)
                const text = beforeTrans(row.en)
                // if(true){
                    google.translate({text: text, from:"en", to:'es'}).then(r => {
                        if(r && r.result[0]){
                            const data = afterTrans(r.result[0])
                            console.log(data)
                            db.run("UPDATE lang SET es = ? WHERE id = ?", data, row.id);
                        }
                    });
                // }
                // if(true){
                    google.translate({text:text, from:"en", to:'ko'}).then(r => {
                        if(r && r.result[0]){
                            const data = afterTrans(r.result[0])
                            console.log(data)
                            db.run("UPDATE lang SET ko = ? WHERE id = ?",  data, row.id);
                        }
                    });
                // }
            })
        }
        if(e){
            console.log(e)
        }
    })
}

// wait()
console.log(afterTrans("% 1 $ s 이 (가) % 3 $ s 에서  % 2 $ s  영구 지문 액세스를 취소했습니다."))