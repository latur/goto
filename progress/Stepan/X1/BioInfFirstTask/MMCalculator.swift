//  Created by Stepan on 20/07/16.

import Foundation

class MMCalculator {
    static func calculate (reads: [String], inout chain: [String: Float], degree: Int) {
        var lesserCount: [String: Float] = [:]
        
        for read in reads {
            //K-ном без последнего
            var part = String(read.characters.prefix(degree-1))
            
            for character in read.characters.dropFirst(degree-1) {
                //Подчет количества K-номов без последнего (для деления)
                if lesserCount[part] == nil {
                    lesserCount[part] = 1
                }
                else {
                    lesserCount[part]! += 1
                }
                
                //Подсчет количества К-номов
                let kPart: String = part+String(character)
                if chain[kPart] == nil {
                    chain[kPart] = 1
                }
                else {
                    chain[kPart]! += 1
                }
                
                //Добавляем символ к К-ному
                changePart(&part, withAdditionalChar: character)
            }
        }
        
        //Вычисление вероятности
        for (key, value) in chain {
            //Долго
            if let qty = lesserCount[String(key.characters.dropLast())] {
                chain[key] = value/qty
            }
            else {
                print("kek")
                chain[key] = 1
            }
        }
    }
    
    private static func changePart (inout part: String, withAdditionalChar char: Character) {
        part = String(part.characters.dropFirst())+String(char)
    }

}
