class OrderDataType:

    response_type = {"치킨": [{"교촌치킨": ["후라이드", "양념", "후라이드 반 양념 반", "간장"]},
                            {"BBQ": ["후라이드", "양념", "후라이드 반 양념 반", "간장"]},
                            {"BHC": ["후라이드", "양념", "후라이드 반 양념 반", "간장"]},
                            {"굽네치킨": ["후라이드", "양념", "후라이드 반 양념 반", "간장"]}],

                     "피자": [{"도미노피자": ["콤비네이션", "불고기", "쉬림프", "고구마"]},
                            {"피자알볼로": ["콤비네이션", "불고기", "쉬림프", "고구마"]},
                            {"피자헛": ["콤비네이션", "불고기", "쉬림프", "고구마"]},
                            {"미스터피자": ["콤비네이션", "불고기", "쉬림프", "고구마"]}],

                     "족발": [{"오풍미족발": ["족발", "양념족발", "매운족발", "마늘족발"]},
                            {"족발신선생": ["족발", "양념족발", "매운족발", "마늘족발"]},
                            {"1일족발": ["족발", "양념족발", "매운족발", "마늘족발"]},
                            {"가장맛있는족발": ["족발", "양념족발", "매운족발", "마늘족발"]}],

                     "떡볶이": [{"엽기떡볶이": ["떡볶이", "짜장떡볶이", "매운떡볶이", "로제떡볶이"]},
                             {"신전떡볶이": ["떡볶이", "짜장떡볶이", "매운떡볶이", "로제떡볶이"]},
                             {"두끼": ["떡볶이", "짜장떡볶이", "매운떡볶이", "로제떡볶이"]},
                             {"죠스떡볶이": ["떡볶이", "짜장떡볶이", "매운떡볶이", "로제떡볶이"]}],

                     "버거": [{"버거킹": ["불고기버거", "새우버거", "치즈버거", "핫크리스피버거"]},
                            {"롯데리아": ["불고기버거", "새우버거", "치즈버거", "핫크리스피버거"]},
                            {"맥도날드": ["불고기버거", "새우버거", "치즈버거", "핫크리스피버거"]},
                            {"노브랜드버거": ["불고기버거", "새우버거", "치즈버거", "핫크리스피버거"]}]}

    food_type = ""
    brand_type = ""
    meny_type = ""
    person_type = 0
    time_type = [15, 30, 45, 60]
