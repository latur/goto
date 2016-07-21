//  Created by Stepan on 19/07/16.

import Foundation

class GCContentCalc {
    static func calculate (read: String) -> Float {
        var percentage: Float = 0.0
        
        var gCount: Int = 0
        var cCount: Int = 0
        
        for character in read.characters {
            switch character {
                case "G": gCount += 1
                case "C": cCount += 1
                case "g": gCount += 1
                case "c": cCount += 1
            default : break
            }
        }
        let sz = Float(read.characters.count)
        percentage = Float(gCount+cCount)/sz
        
        return percentage
    }
}
