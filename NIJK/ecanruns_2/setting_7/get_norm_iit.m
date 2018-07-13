function [ iit, iit_normalized ] = get_norm_iit( iit_sys, cov1, cov2, iit_a, iit_b, eps )
%UNTITLED6 Summary of this function goes here
%   Detailed explanation goes here
    covars = [cov1, cov2];
    L = 0.5*log2(max(min(covars), eps));
    iit = iit_sys + iit_a + iit_b;
    iit_normalized = (iit_sys + iit_a + iit_b)/L;

    
end

