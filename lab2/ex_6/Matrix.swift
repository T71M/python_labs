//
//  Matrix.swift
//  ex_2
//
//  Created by 71M on 11.12.2021.
//

import Foundation


class Matrix {
     var data = [[Double]]();
    
    init(){
        for i in 0...4{
            data.append([])
            for _ in 0...4{
                data[i].append(0.0);
            }
        }
    }
    
    init(array:[[Double]]){
        data = array;
    }
    
    func at( i:Int,  j:Int) -> Double{
        return data[i][j];
    }
    
    func setAt(i:Int,  j:Int, val:Double){
        data[i][j] = val;
    }
    
    func display(){
        print(data);
    }
    
    
    
    
}
