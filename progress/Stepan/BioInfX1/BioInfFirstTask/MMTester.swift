//  Created by Stepan on 20/07/16.

import Foundation

class MMTester {
    static func test (testData data: [String: [String]], degree: Int, possibilities: [String: [String: Float]]) -> String {
        var result = ""
        
        var eLogProb: Float = 0
        var cLogProb: Float = 0
        
        for read in data["X"]! {
            var part = String(read.characters.prefix(degree-1))
            
            for character in read.characters.dropFirst(degree-1) {
                
                //TODO: убрать копипаст
                let ePartProb = possibilities["E"]![part+String(character)]
                
                if ePartProb == nil {
                    eLogProb -= 9999//log(1)
                }
                else {
                    eLogProb += log(ePartProb!)
                }
               
                let cPartProb = possibilities["C"]![part+String(character)]
                
                if cPartProb == nil {
                    cLogProb -= 9999//log(1)
                }
                else {
                    cLogProb += log(cPartProb!)
                }
                
                changePart(&part, withAdditionalChar: character)
            }
            
            if eLogProb > cLogProb {
                result += "E "
            }
            else {
                result += "C "
            }
            
        }
        return result
    }
    
    private static func changePart (inout part: String, withAdditionalChar char: Character) {
        part = String(part.characters.dropFirst())+String(char)
    }
}