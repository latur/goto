//  Created by Stepan on 20/07/16.

import Foundation

class MMCalculator {
    static func calculate (reads: [String], inout chain: [String: Float], degree: Int) {
        var lesserCount: [String: Float] = [:]
        
        for read in reads {
            var part = String(read.characters.prefix(degree-1))
            
            for character in read.characters.dropFirst(degree-1) {
                if lesserCount[part] == nil {
                    lesserCount[part] = 1
                }
                else {
                    lesserCount[part]! += 1
                }
                
                let kPart: String = part+String(character)
                if chain[kPart] == nil {
                    chain[kPart] = 1
                }
                else {
                    chain[kPart]! += 1
                }
                changePart(&part, withAdditionalChar: character)
            }
        }
        
        for (key, value) in chain {
            if let qty = lesserCount[String(key.characters.dropLast())] {
                chain[key] = value/qty
            }
            else {
                chain[key] = 1
            }
        }
    }
    
    private static func changePart (inout part: String, withAdditionalChar char: Character) {
        part = String(part.characters.dropFirst())+String(char)
    }

}
