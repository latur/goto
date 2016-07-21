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
                    eLogProb += log(1)
                }
                else {
                    eLogProb += log(ePartProb!)
                }
               
                let cPartProb = possibilities["C"]![part+String(character)]
                
                if cPartProb == nil {
                    cLogProb += log(1)
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
//        for read in data["X"]! {
//            let prob = calculate(read, degree: 4)
//
//            if abs(prob-trainProbs.eLogProb) > abs(prob-trainProbs.cLogProb) {
//                result += "C "
//            }
//            else {
//                result += "E "
//            }
//        }
    
//    private static func calculate (read: String, degree: Int) -> Float {
//        var chain: [String: Float] = [:]
//        var lesserCount: [String: Float] = [:]
//        
//        var part = String(read.characters.prefix(degree-1))
//        
//        for character in read.characters.dropFirst(degree-1) {
//            if lesserCount[part] == nil {
//                lesserCount[part] = 1
//            }
//            else {
//                lesserCount[part]! += 1
//            }
//            
//            let kPart: String = part+String(character)
//            if chain[kPart] == nil {
//                chain[kPart] = 1
//            }
//            else {
//                chain[kPart]! += 1
//            }
//            changePart(&part, withAdditionalChar: character)
//            
//        }
//        
//        for (key, value) in chain {
//            if let qty = lesserCount[String(key.characters.dropLast())] {
//                chain[key] = value/qty
//            }
//            else {
//                chain[key] = 1
//            }
//        }
//        
//        var logProb: Float = 0
//        for (_, value) in chain {
//            logProb += log(value)
//        }
//        
//        return logProb
//    }
//    
    private static func changePart (inout part: String, withAdditionalChar char: Character) {
        part = String(part.characters.dropFirst())+String(char)
    }
}