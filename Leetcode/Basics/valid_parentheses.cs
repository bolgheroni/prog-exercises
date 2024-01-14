using System;
using System.Collections.Generic;

public class Solution {
    
    public bool isWellFormed(char parOpen, char parClose) {
        if (parOpen == '(' && parClose == ')') {
            return true;
        }
        if (parOpen == '{' && parClose == '}') {
            return true;
        }
        if (parOpen == '[' && parClose == ']') {
            return true;
        }

        return false;
    }

    public bool isOpenPar(char c) {
        if (c == '(' || c == '{' || c == '['){
            return true;
        }
        return false;
    }

    public bool IsValid(string s) {
        Stack<char> pars = new Stack<char>();

        for (int i = 0; i< s.Length; i++ ) {
            char currentPar = s[i];
            
            if (isOpenPar(currentPar)) {
                pars.Push(currentPar);
            } else {
                if (pars.Count == 0) {
                    return false;
                }
                char topChar = pars.Pop();
                if (!isWellFormed(topChar, currentPar)) {
                    return false;
                }
            }

        }
        if (pars.Count > 0) {
            return false;
        }
        return true;
    }
}