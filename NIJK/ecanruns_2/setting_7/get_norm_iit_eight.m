function [ iit, iit_normalized ] = get_norm_iit_eight( iit_sys, cov1, cov2, cov3, iit_a, iit_b, iit_c, eps )
%UNTITLED6 Summary of this function goes here
%   Detailed explanation goes here
    covars = [cov1, cov2, cov3];
    my_min = min(covars);
    if my_min == 0
        my_min = eps;
    end
    L = 0.5*log2(my_min);
    if L == 0
        L = eps;
    end
    iit = iit_sys + iit_a + iit_b + iit_c;
    iit_normalized = (iit_sys + iit_a + iit_b + iit_c)/L;

    
end

