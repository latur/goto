//  Created by Stepan on 19/07/16.

import Foundation

class GCContentCalc {
    static func calculate (read: String) -> Float {
        var percentage: Float = 0.0
        
        var gCount: Float = 0
        var cCount: Float = 0
        
        for character in read.characters {
            switch String(character).uppercaseString {
                case "G": gCount += 1
                case "C": cCount += 1
            default : break
            }
        }
        percentage = (gCount+cCount)/Float(read.characters.count)
        
        return percentage
    }
}
