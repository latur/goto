//  Created by Stepan on 21/07/16.

import Foundation

class GCCTrainer {
    static func train (data: [String], degree: Int) -> [Float] {
        var hystogram: [Float] = []
        
        let anyRead = data[0]
        let count: Float = Float(anyRead.characters.count)
        
        var endIndex: Int = 0
        var part: String = ""

        for index in 0..<anyRead.characters.dropFirst(degree-1).count {
            
            endIndex = index+degree
            let range = anyRead.startIndex.advancedBy(index)..<anyRead.startIndex.advancedBy(endIndex)
    
            for read in data {
                part = read.substringWithRange(range)
                hystogram.append(GCContentCalc.calculate(part))
            }
//            guard (hystogram.last != nil) else {
//                print ("last doesn't exist")
//                exit(228)
//            }
            hystogram.append(hystogram.popLast()!/count)
        }
        
        return hystogram
    }
}


