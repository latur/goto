//  Created by Stepan on 21/07/16.

import Foundation

class GCCTrainer {
    static func train (data: [String], degree: Int) -> [Float] {
        var hystogram: [Float] = []
        
        var tempGCC: Float = 0
        
        let anyRead = data[0]
        let count: Float = Float(anyRead.characters.count)
        
        var endIndex: Int = 0
        var part: String = ""

        let sz = anyRead.characters.count
        
        for index in 0..<sz {
            
            endIndex = index+degree
            //  может быть ошибка тут
            let range = anyRead.startIndex.advancedBy(index)..<anyRead.startIndex.advancedBy(endIndex)
            
            for read in data {
                part = read.substringWithRange(range)
                tempGCC += GCContentCalc.calculate(part, degree: degree)
            }
//            guard (hystogram.last != nil) else {
//                print ("last doesn't exist")
//                exit(228)
//            }
            hystogram.append(tempGCC/count)
            tempGCC = 0
            
            print ("  \(Float(index)/Float(sz))%, \(sz)")
            
        }
        
        return hystogram
    }
}


