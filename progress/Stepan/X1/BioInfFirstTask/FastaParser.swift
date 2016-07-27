//  Created by Stepan on 19/07/16.

import Foundation

class FastaParser {
    static func parse (path: String) -> [String: [String]] {
        guard let file = fileManager.contentsAtPath(path) else {
            print ("  Wrong file")
            exit(228)
        }
        
        guard let datastring = NSString(data: file, encoding: NSUTF8StringEncoding) else {
            print("  File error")
            exit(228)
        }
        
        var parsedCode: [String: [String]] = [:]
        
        let lines = datastring.componentsSeparatedByCharactersInSet(NSCharacterSet.newlineCharacterSet())
        var currentType = "err"
        for line in lines {
            if String(line[line.startIndex]) == ">" {
                currentType = String(line[line.startIndex.successor()])
            }
            else {
                if parsedCode[currentType] == nil {
                    parsedCode[currentType] = []
                }
                parsedCode[currentType]!.append(line)
            }
        }
        print ("  Parsed data.\n")
        return parsedCode
    }
}
